 var flashcards = JSON.parse(document.getElementById('flashcards-data').textContent);
        let current = 0;
        function showFlashcard(idx) {
            document.getElementById('question').textContent = flashcards[idx].question;
            document.getElementById('answer').textContent = flashcards[idx].answer;
            document.getElementById('flashcard').classList.remove('flipped');
        }
        document.getElementById('flip-btn').onclick = function() {
            document.getElementById('flashcard').classList.toggle('flipped');
        };

        document.getElementById('next-btn').onclick = function() {
            document.getElementById('flashcard').classList.remove('flipped');
            setTimeout(function() {
                current = Math.floor(Math.random() * flashcards.length);
                showFlashcard(current);
            }, 400); 
        };

        window.onload = function() { showFlashcard(current); };