function init() {
    accordionToggle();
}

function accordionToggle(){
    var accordions = document.getElementsByClassName("accordion");

    for (var i = 0; i < accordions.length; i++) {
        accordions[i].onclick = function () {
            this.classList.toggle('is-open');
            var accordionContent = this.nextElementSibling;

            if(accordionContent.style.maxHeight) {
                // accordion toggle open
                accordionContent.style.maxHeight = null;
            } else {
                // accordion toggle close
                accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
            }
        }
    }
}

window.onload = init();