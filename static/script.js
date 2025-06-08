
document.getElementById('toggle-mode').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');
});

function analyser() {
    fetch("/api/analyse", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            exclude: document.getElementById("exclude").value,
            jour: document.getElementById("jour").value,
            date_debut: document.getElementById("date_debut").value,
            date_fin: document.getElementById("date_fin").value,
        })
    }).then(res => res.json()).then(data => {
        document.getElementById("resultats").innerText = JSON.stringify(data, null, 2);
    }).catch(err => {
        document.getElementById("resultats").innerText = "Erreur : " + err;
    });
}
