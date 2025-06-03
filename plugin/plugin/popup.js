document.getElementById("analyze").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "getSelection" }, (response) => {
      if (!response || !response.text) {
        document.getElementById("output").innerText = "❌ Kein Text ausgewählt.";
        return;
      }

      // Dein Prompt-Template
      const prompt = `[INST] Please extract the base risk, the new absolute risk, and the relative risk from the following sentence:\n\n${response.text}\n\nFormat:\nbase risk: ...\nnew absolute risk: ...\nrelative risk: ...\n[/INST]`;

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
    });
  });
});