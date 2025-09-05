window.onload = function() {
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
            const card = document.getElementById('flashcard');
            card.classList.remove('flipped');
            card.classList.add('flashcard-animate-out');            
            
            setTimeout(function() {
                let novo;
                do {
                    novo = Math.floor(Math.random() * flashcards.length);
                } while (ultimos.includes(novo) && ultimos.length < flashcards.length);
                current = novo;
                ultimos.push(current);
                if (ultimos.length > 10) ultimos.shift();
                showFlashcard(current);
                card.classList.remove('flashcard-animate-out');
                card.classList.add('flashcard-animate-in');
                setTimeout(() => card.classList.remove('flashcard-animate-in'), 400);
            }, 400);
        };

        // document.getElementById('next-btn').onclick = function() {
        //     document.getElementById('flashcard').classList.remove('flipped');
        //     setTimeout(function() {
        //         let novo;
        //         do {
        //             novo = Math.floor(Math.random() * flashcards.length);
        //         } while (ultimos.includes(novo) && ultimos.length < flashcards.length);
        //         current = novo;
        //         ultimos.push(current);
        //         if (ultimos.length > 10) ultimos.shift();
        //         console.log('Últimos índices:', ultimos); 
        //         showFlashcard(current);
        //     }, 400);
        // };
  showFlashcard(current);
};
        // window.onload = function() { showFlashcard(current); };