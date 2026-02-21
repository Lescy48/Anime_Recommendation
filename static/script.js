let selectedGenres = [];
let currentResults = [];

// ── WARNING MODAL ──
function showWarning() {
    document.getElementById('warningOverlay').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeWarning(e) {
    if (e.target === document.getElementById('warningOverlay')) {
        _closeWarning();
    }
}

function closeWarningBtn() {
    _closeWarning();
}

function _closeWarning() {
    document.getElementById('warningOverlay').classList.remove('active');
    document.body.style.overflow = '';
}

// ── GENRE ──
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
    el.textContent = selectedGenres.length === 0 ? '' : `${selectedGenres.length} genre dipilih`;
}

function resetAll() {
    selectedGenres = [];
    document.querySelectorAll('.genre-btn.active').forEach(b => b.classList.remove('active'));
    updateCount();
    document.getElementById('resultsSection').style.display = 'none';
    document.getElementById('noResults').style.display = 'none';
}

// ── SEARCH ──
async function searchAnime() {
    if (selectedGenres.length === 0) {
        showWarning();
        return;
    }

    document.getElementById('loading').style.display = 'flex';
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
    } catch {
        showWarning();
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
    document.getElementById('resultsCount').innerHTML = `<strong>${data.length}</strong> anime ditemukan`;

    if (data.length === 0) {
        document.getElementById('noResults').style.display = 'block';
        return;
    }

    document.getElementById('resultsSection').style.display = 'block';
    document.getElementById('sortSelect').value = 'match';
    renderCards(data);
}

function renderCards(data) {
    const list = document.getElementById('animeList');
    list.innerHTML = '';

    data.forEach(anime => {
        const safeId = anime.title.replace(/[^a-zA-Z0-9]/g, '_');
        const hasImage = anime.image_url && anime.image_url !== '';

        const genreTags = anime.genres.split(', ').map(g => {
            const isMatched = selectedGenres.includes(g);
            return `<span class="genre-tag ${isMatched ? 'matched' : ''}">${g}</span>`;
        }).join('');

        const card = document.createElement('div');
        card.className = 'anime-card';
        card.onclick = () => openModal(anime);
        card.innerHTML = `
            <div class="anime-card-img-wrapper">
                ${hasImage
                    ? `<img class="anime-card-img"
                            src="${anime.image_url}"
                            alt="${anime.title}"
                            loading="lazy"
                            onerror="this.style.display='none';document.getElementById('ph-${safeId}').style.display='flex';">`
                    : ''
                }
                <div class="img-placeholder" id="ph-${safeId}"
                     style="${hasImage ? 'display:none' : 'display:flex'}">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                         stroke="currentColor" stroke-width="1.2" opacity="0.4">
                        <rect x="3" y="3" width="18" height="18" rx="2"/>
                        <circle cx="8.5" cy="8.5" r="1.5"/>
                        <polyline points="21 15 16 10 5 21"/>
                    </svg>
                </div>
            </div>
            <div class="anime-card-body">
                <div class="anime-card-title">${anime.title}</div>
                <div class="anime-meta">
                    <div class="anime-rating">
                        <span class="rating-star">★</span>
                        <span class="rating-num">${anime.rating.toFixed(1)}</span>
                    </div>
                    <span class="match-badge">${anime.match_count} genre cocok</span>
                </div>
                <div class="anime-genres">${genreTags}</div>
                <div class="anime-synopsis-short">${anime.synopsis}</div>
                <button class="read-more">Lihat synopsis lengkap</button>
            </div>
        `;
        list.appendChild(card);
    });
}

// ── MODAL ANIME ──
function openModal(anime) {
    const overlay = document.getElementById('modalOverlay');
    const hasImage = anime.image_url && anime.image_url !== '';

    const modalImg = document.getElementById('modalImg');
    const modalImgPlaceholder = document.getElementById('modalImgPlaceholder');

    if (hasImage) {
        modalImg.src = anime.image_url;
        modalImg.alt = anime.title;
        modalImg.classList.remove('hidden');
        modalImgPlaceholder.style.display = 'none';
    } else {
        modalImg.classList.add('hidden');
        modalImgPlaceholder.style.display = 'flex';
    }

    document.getElementById('modalTitle').textContent = anime.title;

    document.getElementById('modalMeta').innerHTML = `
        <div class="anime-rating">
            <span class="rating-star">★</span>
            <span class="rating-num">${anime.rating.toFixed(1)}</span>
        </div>
        <span class="match-badge">${anime.match_count} genre cocok</span>
    `;

    document.getElementById('modalGenres').innerHTML = anime.genres.split(', ').map(g => {
        const isMatched = selectedGenres.includes(g);
        return `<span class="genre-tag ${isMatched ? 'matched' : ''}">${g}</span>`;
    }).join('');

    document.getElementById('modalSynopsis').textContent = anime.synopsis;

    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal(e) {
    if (e.target === document.getElementById('modalOverlay')) {
        _closeModal();
    }
}

function closeModalBtn() {
    _closeModal();
}

function _closeModal() {
    document.getElementById('modalOverlay').classList.remove('active');
    document.body.style.overflow = '';
}

// ── KEYBOARD ──
document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
        _closeModal();
        _closeWarning();
    }
});

// ── HEADER CLICK ──
document.querySelector('header h1').addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
});