document.getElementById("analyze").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "getSelection" }, (response) => {
      if (!response || !response.text) {
        document.getElementById("output").innerText = "❌ Kein Text ausgewählt.";
        return;
      }

      const prompt = response.text;

      // Originaler Server-Aufruf (auskommentiert)
      /*
      fetch("http://193.196.39.49:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: prompt })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("output").innerText = data.response || "Keine Antwort erhalten.";
      })
      .catch(err => {
        document.getElementById("output").innerText = "❌ Fehler beim Abrufen der API.";
        console.error(err);
      });
      */

      // Dummy-Funktion als Ersatz für Server-Antwort
      function analyzeTextDummy(text) {
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve({ response: `Simulierte Antwort für: "${text}"` });
          }, 300); // Verzögerung simuliert Netzwerk
        });
      }

      // Dummy-Aufruf
      analyzeTextDummy(prompt).then(data => {
        document.getElementById("output").innerText = data.response;
      });

    });
  });
});