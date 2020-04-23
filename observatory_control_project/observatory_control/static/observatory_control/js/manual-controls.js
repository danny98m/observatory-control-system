function init() {
    accordionToggle();
    switchToggle();
}

function accordionToggle(){
    var accordions = document.getElementsByClassName('accordion');

    for (var i = 0; i < accordions.length; i++) {
        accordions[i].onclick = function () {
            var accordionContent = this.nextElementSibling;

            if(this.classList.contains('is-open')) {
                // accordion toggle open
                accordionContent.style.maxHeight = 0;
            } else {
                // accordion toggle close
                accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
                // accordionContent.scrollHeight + "px"
            }
            this.classList.toggle('is-open');
        }
    }
}

function switchToggle() {
    var switches = document.getElementsByClassName('switch-input');

    switches[0].onclick = function () {
        if(switches[0].checked) {
            switches[1].checked = true;
            switches[2].checked = true;
        } else {
            switches[1].checked = false;
            switches[2].checked = false;
        }
    }

    for (var i = 1; i < switches.length; i++) {
        switches[i].onclick = function () {
            let sideA = switches[1].checked
            let sideB = switches[2].checked

            if((sideA && sideB) || !(sideA || sideB)) {
                switches[0].disabled = false;
            } else {
                switches[0].disabled = true;
            }

            if (sideA && sideB) {
                switches[0].checked = true;
            } 
            else if (!(sideA || sideB)) {
                switches[0].checked = false;
            }
        }
    }
}

window.onload = init();