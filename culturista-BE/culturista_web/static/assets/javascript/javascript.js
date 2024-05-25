
/*hiệu ứng cho navbar*/
$(document).ready(function() {
    $(window).scroll(function() {
            if ($(this).scrollTop()) {
                $('header').addClass('sticky');
            } else {
                $('header').removeClass('sticky');
            }
    });
});

/*hiệu ứng cho backgr img và chữ*/
$(document).ready(function() {
    $(window).scroll(function() {
        const scrollPosition = $(this).scrollTop();
        
        const bgMoveAmount = scrollPosition * 0.2; 
        $('.slider__bg').css('transform', `translateY(-${bgMoveAmount}px)`);
        
        const leftImgMoveAmount = scrollPosition * 0.5; 
        $('.slider__img--left').css('transform', `translate(-${leftImgMoveAmount}px, -50%)`);
        
        const rightImgMoveAmount = scrollPosition * 0.5; 
        $('.slider__img--right').css('transform', `translate(${rightImgMoveAmount}px, -50%)`);
        
        const contentMoveAmount = scrollPosition * 0.3; 
        $('.slider__content').css('transform', `translateX(-${contentMoveAmount}px)`);
    });
});

let scrollContainer = document.querySelector(".gallery");
let backBtn = document.getElementById("backBtn");
let nextBtn = document.getElementById("nextBtn");

scrollContainer.addEventListener("wheel",(evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
});

nextBtn.addEventListener("click", () =>{
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft += 900;
});

backBtn.addEventListener("click", () =>{
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft -= 900;
});

    

// Sự kiện khi nhấn vào nút menu-icon
document.querySelector('.menu-icon').addEventListener('click', function() {
    // Thêm hoặc xóa lớp 'show' của ul#main-menu
    document.querySelector('ul#main-menu').classList.toggle('show');
});


