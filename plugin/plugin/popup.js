function highlightKeyPhrases(text) {
  // Warnungen wie vorher
  const warningPattern = /^.*Warning:.*$/gm;
  text = text.replace(warningPattern, match => {
    return `<div class="highlight warning">${match}</div>`;
  });

  // Transparenz-Phrasen wie gewünscht
  const transparentPattern = /^.*Risk communication transparent\..*$/gm;
  text = text.replace(transparentPattern, match => {
    return `<div class="highlight info">${match}</div>`;
  });
   // 3. Titel-Zeilen wie --- Some Heading ---
  const headingPattern = /^--- (.*?) ---$/gm;
  text = text.replace(headingPattern, (match, title) => {
    return `<strong>--- ${title} ---</strong>`;
  });
  return text;
}
document.getElementById("analyze").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (!tabs || tabs.length === 0) {
      document.getElementById("output").innerText = "❌ Kein aktiver Tab gefunden.";
      return;
    }

    const tabId = tabs[0].id;

    chrome.tabs.sendMessage(tabId, { action: "getSelection" }, (response) => {
      if (chrome.runtime.lastError) {
        console.error("Fehler beim Senden der Nachricht:", chrome.runtime.lastError.message);
        document.getElementById("output").innerText = "❌ Fehler beim Zugriff auf die Seite. Evtl. keine unterstützte Seite.";
        return;
      }

      if (!response || typeof response.text !== "string" || response.text.trim() === "") {
        document.getElementById("output").innerText = "❌ Kein Text ausgewählt.";
        return;
      }

      const selectedText = response.text.trim();

const prompt = `Two Risk Scenarios

--- Calculating missing figures ---
From relative risk and base absolute risk calculated: absolute risk (new) = 10.00%

--- Qualitative Assessment ---
Sources provided – please verify:
     • Source for base risk: clinical trial A
     • Source for new risk: clinical trial B
Warning: Verbal risk descriptors present. Please verify definitions for:
     • verbal_risk_descriptor_change: significantly higher

--- Missing Values Check ---
Both absolute risks calculable. Risk communication transparent.

--- Transparent Presentation ---
Absolute risk (base): 5.00% (5.00 per 100)
Absolute risk (new): 10.00% (10.00 per 100)
The risk in the new case is 100.00% higher than in the base case.`;

   
      // Originaler Server-Aufruf (auskommentiert, zum Testen mit Dummy gearbeitet)
      /*
      fetch("http://193.196.39.49:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: prompt })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("output").innerHTML = data.response || "Keine Antwort erhalten.";
      })
      .catch(err => {
        document.getElementById("output").innerHTML = "❌ Fehler beim Abrufen der API.";
        console.error(err);
      });
      */

      // Dummy-Funktion als Ersatz für Server-Antwort
      function analyzeTextDummy(text) {
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve({ response: text });
          }, 300); // Verzögerung simuliert Netzwerk
        });
      }

      // Dummy-Aufruf
      analyzeTextDummy(prompt).then(data => {
        const outputElement = document.getElementById("output");
        outputElement.innerHTML = highlightKeyPhrases(data.response).replace(/\n/g, "<br>");
        outputElement.classList.remove("animated");      // vorherige Animation entfernen
        void outputElement.offsetWidth;                  // Trick: Reflow zum Neustarten der Animation
        outputElement.classList.add("animated");         // Klasse für Animation hinzufügen
      });

    });
  });
});
