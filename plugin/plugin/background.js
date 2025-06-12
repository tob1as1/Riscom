chrome.action.onClicked.addListener(() => {
  chrome.windows.create({
    url: "popup.html",
    type: "popup",
    width: 400,
    height: 600,
    top: 100,   // Fenster-Position (optional)
    left: 100
  });
});
