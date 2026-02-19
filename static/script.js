let selectedGenres = [];
let currentResults = [];

function toggleGenre(btn) {
    const genre = btn.dataset.genre;
    if (btn.classList.contains('active')) {
        btn.classList.remove('active');
        selectedGenres = selectedGenres.filter(g => g !== genre);
    } else {
        btn.classList.add('active');
        selectedGenres.push(genre);
    }
    updateCount();
}

function updateCount() {
    const el = document.getElementById('selectedCount');
    el.textContent = selectedGenres.length === 0
        ? '0 genre dipilih'
        : `${selectedGenres.length} genre dipilih: ${selectedGenres.join(', ')}`;
}

function resetAll() {
    selectedGenres = [];
    document.querySelectorAll('.genre-btn.active').forEach(b => b.classList.remove('active'));
    updateCount();
    document.getElementById('resultsSection').style.display = 'none';
    document.getElementById('noResults').style.display = 'none';
}

async function searchAnime() {
    if (selectedGenres.length === 0) {
        alert('Pilih minimal satu genre dulu ya!');
        return;
    }

    document.getElementById('loading').style.display = 'block';
    document.getElementById('resultsSection').style.display = 'none';
    document.getElementById('noResults').style.display = 'none';

    try {
        const res = await fetch('/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ genres: selectedGenres })
        });
        const data = await res.json();
        currentResults = data;
        displayResults(data);
    } catch (err) {
        alert('Terjadi error. Coba lagi!');
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}

function sortResults() {
    const sortBy = document.getElementById('sortSelect').value;
    let sorted = [...currentResults];
    if (sortBy === 'rating_desc') sorted.sort((a, b) => b.rating - a.rating);
    else if (sortBy === 'rating_asc') sorted.sort((a, b) => a.rating - b.rating);
    else if (sortBy === 'title') sorted.sort((a, b) => a.title.localeCompare(b.title));
    else sorted.sort((a, b) => b.match_count - a.match_count || b.rating - a.rating);
    renderCards(sorted);
}

function displayResults(data) {
    document.getElementById('resultsCount').textContent = `${data.length} anime ditemukan`;

    if (data.length === 0) {
        document.getElementById('noResults').style.display = 'block';
        return;
    }

    document.getElementById('resultsSection').style.display = 'block';
    document.getElementById('sortSelect').value = 'match';
    renderCards(data);
}

function renderCards(data) {
    const grid = document.getElementById('animeGrid');
    grid.innerHTML = '';

    data.forEach(anime => {
        const genreTags = anime.genres.split(', ').map(g => {
            const isMatched = selectedGenres.includes(g);
            return `<span class="genre-tag ${isMatched ? 'matched' : ''}">${g}</span>`;
        }).join('');

        const card = document.createElement('div');
        card.className = 'anime-card';
        card.innerHTML = `
            <img class="anime-card-img"
                 src="${anime.image_url}"
                 alt="${anime.title}"
                 onerror="this.src='https://via.placeholder.com/220x280/161b22/8b949e?text=No+Image'">
            <div class="anime-card-body">
                <div class="anime-card-title">${anime.title}</div>
                <div class="anime-rating">
                    <span class="star">★</span>
                    <span class="rating-num">${anime.rating.toFixed(1)}</span>
                </div>
                <div class="match-badge">✓ ${anime.match_count} genre cocok</div>
                <div class="anime-genres">${genreTags}</div>
                <div class="anime-synopsis">${anime.synopsis}</div>
            </div>
        `;
        grid.appendChild(card);
    });
}