<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\CHEMISTRY\chemistry_metrics.md -->




[Home](/index.html)

---
layout: default
---

# Data from CSV

SI prefixes

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/SI_Prefixes.csv" download="SI_Prefixes.csv">Download SI Prefixes CSV</a></p>

<div id="csv-content1">Loading data...</div>

<script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.0/papaparse.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/SI_Prefixes.csv", {
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



Unit conversions for derived SI units

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Derived_SI_Units_Conversions.csv" download="Derived_SI_Units_Conversions.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content2">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Derived_SI_Units_Conversions.csv", {
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
            document.getElementById('csv-content2').innerHTML = content;
        }
    });
});
</script>





Conversion factors for non-SI units

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Non_SI_Units_Conversions.csv" download="Non_SI_Units_Conversions.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content3">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Non_SI_Units_Conversions.csv", {
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
            document.getElementById('csv-content3').innerHTML = content;
        }
    });
});
</script>







Fundamental constants

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Fundamental_Constants.csv" download="Fundamental_Constants.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content4">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Fundamental_Constants.csv", {
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
            document.getElementById('csv-content4').innerHTML = content;
        }
    });
});
</script>








General solubility rules for ionic compounds in water

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/General_Solubility_Rules_Ionic_Compounds.csv" download="General_Solubility_Rules_Ionic_Compounds.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content6">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/General_Solubility_Rules_Ionic_Compounds.csv", {
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
            document.getElementById('csv-content5').innerHTML = content;
        }
    });
});
</script>







Solubility of ionic compounds in water

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Solubility_Ionic_Compounds.csv" download="Solubility_Ionic_Compounds.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content7">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Solubility_Ionic_Compounds.csv", {
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
            document.getElementById('csv-content6').innerHTML = content;
        }
    });
});
</script>







Metal activity series

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Metal_Activity_Series.csv" download="Metal_Activity_Series.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content8">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Metal_Activity_Series.csv", {
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
            document.getElementById('csv-content7').innerHTML = content;
        }
    });
});
</script>







Phase change properties of pure substances

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Phase_Change_Properties.csv" download="Phase_Change_Properties.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content9">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Phase_Change_Properties.csv", {
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
            document.getElementById('csv-content8').innerHTML = content;
        }
    });
});
</script>








Molar freezing point depression and boiling point elevation constants

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Molal_Properties.csv" download="Molal_Properties.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content10">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Molal_Properties.csv", {
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
            document.getElementById('csv-content9').innerHTML = content;
        }
    });
});
</script>




Bond Energies

<!-- Download link for the CSV file -->
<p><a href="/assets/chemistry_data/Bond_Energies.csv" download="Bond_Energies.csv">Download Derived_SI_Units_Conversions CSV</a></p>

<div id="csv-content11">Loading data...</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    Papa.parse("/assets/chemistry_data/Bond_Energies.csv", {
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
            document.getElementById('csv-content10').innerHTML = content;
        }
    });
});
</script>






