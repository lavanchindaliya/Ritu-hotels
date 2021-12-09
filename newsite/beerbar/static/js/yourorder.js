var currentPage = "your booking's";
    var navTag = document.querySelector('.order');
    if(currentPage == navTag.innerText.toLowerCase()){
        navTag.style.backgroundColor = '#DC143C'
        navTag.style.color = '#FFF8DC'
    }