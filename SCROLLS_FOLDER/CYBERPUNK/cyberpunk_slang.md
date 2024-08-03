<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\CYBERPUNK\cyberpunk_slang.md -->




[Home](/index.html)

---
layout: default
---

# Data from CSV

Cyberpunk Slang

<!-- Download link for the CSV file -->
<p><a href="/assets/Cyberpunk/cyberpunk_slang.csv" download="cyberpunk_slang">Download Cyberpunk Slang CSV</a></p>

<div id="csv-content1">Loading data...</div>

<script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.0/papaparse.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/Cyberpunk/cyberpunk_slang.csv", {
        download: true,
        header: true,
        complete: function(results) {
            var data = results.data;
            var content = "<table>";
            // Adding table headers
            content += "<tr>";
            for(var key in data[0]) {
                content += "<th>" + key + "</th>";
            }
            content += "</tr>";
            // Adding table data
            for(var i = 0; i < data.length; i++) {
                content += "<tr>";
                for(var key in data[i]) {
                    content += "<td>" + data[i][key] + "</td>";
                }
                content += "</tr>";
            }
            content += "</table>";
            document.getElementById('csv-content1').innerHTML = content;
        }
    });
});
</script>


