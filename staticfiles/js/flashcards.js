window.onload = function () {
  const flashcards = JSON.parse(document.getElementById('flashcards-data').textContent);
  const questionEl = document.getElementById('question');
  const answerEl = document.getElementById('answer');
  const flipBtn = document.getElementById('flip-btn');
  const flipButton = document.getElementById('flip-button');
  const nextBtn = document.getElementById('next-btn');
  const favoriteBtn = document.getElementById('favorite-btn');
  const progressBar = document.getElementById('progress-bar');
  const card = document.getElementById('flashcard');

  let current = -1;
  let ultimos = [];
  let started = false;
  let favorites = new Set();

  // Desativa botões até iniciar
  flipButton.disabled = true;
  nextBtn.disabled = true;
  favoriteBtn.disabled = true;

  function showStartCard() {
    questionEl.innerHTML = '<span style="font-size:1.4rem; font-weight:bold; color:#0078D4; animation:pulse 1.5s infinite; cursor:pointer;">👆 Tap here to start</span>';
    answerEl.textContent = '...';
    card.classList.remove('flipped');
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';
    progressBar.setAttribute('aria-valuenow', 0);
  }

  function showFlashcard(idx) {
    questionEl.textContent = flashcards[idx].question;
    answerEl.textContent = flashcards[idx].answer;
    card.classList.remove('flipped');
    updateProgress(idx);
    updateFavoriteButton(idx);
  }

  function updateProgress(idx) {
    const percent = Math.round(((idx + 1) / flashcards.length) * 100);
    progressBar.style.width = percent + '%';
    progressBar.textContent = `${idx + 1}/${flashcards.length}`;
    progressBar.setAttribute('aria-valuenow', percent);
  }

  function updateFavoriteButton(idx) {
    if (favorites.has(idx)) {
      favoriteBtn.classList.add('active');
      favoriteBtn.textContent = '⭐ Favorito';
    } else {
      favoriteBtn.classList.remove('active');
      favoriteBtn.textContent = '⭐ Favoritar';
    }
  }

  function startFlashcards() {
    if (!started) {
      started = true;
      flipButton.disabled = false;
      nextBtn.disabled = false;
      favoriteBtn.disabled = false;
      nextFlashcard();
    }
  }

  function nextFlashcard() {
    let novo;
    do {
      novo = Math.floor(Math.random() * flashcards.length);
    } while (ultimos.includes(novo) && ultimos.length < flashcards.length);
    current = novo;
    ultimos.push(current);
    if (ultimos.length > 10) ultimos.shift();

    card.classList.remove('flipped');
    card.classList.add('flashcard-animate-out');

    setTimeout(function () {
      showFlashcard(current);
      card.classList.remove('flashcard-animate-out');
      card.classList.add('flashcard-animate-in');
      setTimeout(() => card.classList.remove('flashcard-animate-in'), 400);
    }, 400);
  }

  // Eventos
  flipBtn.onclick = function () {
    if (!started) {
      startFlashcards();
    } else {
      card.classList.toggle('flipped');
    }
  };

  flipButton.onclick = function () {
    if (started) {
      card.classList.toggle('flipped');
    }
  };

  nextBtn.onclick = function () {
    if (started) {
      nextFlashcard();
    }
  };

  favoriteBtn.onclick = function () {
    if (started) {
      if (favorites.has(current)) {
        favorites.delete(current);
      } else {
        favorites.add(current);
      }
      updateFavoriteButton(current);
    }
  };

  // Exibe o cartão inicial ao carregar
  showStartCard();
};