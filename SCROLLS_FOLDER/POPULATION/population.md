<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\POPULATION\population.md -->




[Home](/index.html)

---
layout: default
---

# Data from CSV

American population 

<!-- Download link for the CSV file -->
<p><a href="/assests/population_data/population_wiki.csv" download="population_wiki.csv">Download population_wiki CSV</a></p>

<div id="csv-content1">Loading data...</div>

<script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.0/papaparse.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/population_data/population_wiki.csv", {
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


