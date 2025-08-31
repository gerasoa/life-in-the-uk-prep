 var flashcards = JSON.parse(document.getElementById('flashcards-data').textContent);
        let current = 0;
        let ultimos = [];

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
                let novo;
                do {
                    novo = Math.floor(Math.random() * flashcards.length);
                } while (ultimos.includes(novo) && ultimos.length < flashcards.length);
                current = novo;
                ultimos.push(current);
                if (ultimos.length > 10) ultimos.shift();
                console.log('Últimos índices:', ultimos); 
                showFlashcard(current);
            }, 400);
        };

        window.onload = function() { showFlashcard(current); };