S(document).ready(function() {

    var planetarium = S.virtualsky({
            id: 'starmap',
            projection: 'stereo'
        });

    planetarium.addPointer({
            'ra':83.8220792,
            'dec':-5.3911111,
            'label':'Orion Nebula',
            'img':'http://server7.sky-map.org/imgcut?survey=DSS2&w=128&h=128&ra=5.58813861333333&de=-5.3911111&angle=1.25&output=PNG',
            'url':'http://simbad.u-strasbg.fr/simbad/sim-id?Ident=M42',
            'credit':'Wikisky',
            'colour':'rgb(255,220,220)'
    })


    starmap = document.getElementById('starmap_inner');
    starmap.style.borderRadius = '12px';
    document.getElementById('helpBtn').style.display = 'none';
});

// function searchbar() {
//     var input, filter, ul, li, a, i, txtValue;
//     input = document.getElementById("myInput");
//     filter = input.value.toUpperCase();
//     ul = document.getElementById("myUL");
//     li = ul.getElementsByTagName("li");
//     for (i = 0; i < li.length; i++) {
//         a = li[i].getElementsByTagName("a")[0];
//         txtValue = a.textContent || a.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//             li[i].style.display = "";
//         } else {
//             li[i].style.display = "none";
//         }
//     }
// }