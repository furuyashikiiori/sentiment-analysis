document
  .getElementById("sentiment-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var loadingMessage = document.getElementById("loading-message");
    var resultDiv = document.getElementById("result");
    var inputText = document.getElementById("input-text").value;

    loadingMessage.style.display = "block";
    resultDiv.innerHTML = "";

    fetch("/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: inputText }),
    })
      .then((response) => response.json())
      .then((data) => {
        loadingMessage.style.display = "none";
        resultDiv.innerHTML = "<p>感情分析結果: " + data.sentiment + "</p>";
      })
      .catch((error) => {
        loadingMessage.style.display = "none";
        resultDiv.innerHTML = "<p>エラーが発生しました</p>";
        console.error("Error:", error);
      });
  });
