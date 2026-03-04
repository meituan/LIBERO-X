window.HELP_IMPROVE_VIDEOJS = false;

document.addEventListener('DOMContentLoaded', () => {
  // 获取所有 "navbar-burger" 元素
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // 为每个汉堡菜单添加点击事件
  if ($navbarBurgers.length > 0) {
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {
        // 获取目标菜单元素
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // 切换汉堡菜单和菜单的 active 状态
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }
});

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.episode-desc').forEach((el) => {
    const text = (el.textContent || '').trim();
    if (!text) return;
    let updated = text.charAt(0).toUpperCase() + text.slice(1);
    if (!/[.!?]$/.test(updated)) {
      updated += '.';
    }
    el.textContent = updated;
  });
});


$(document).ready(function() {
    // Check for click events on the navbar burger icon

    var options = {
			slidesToScroll: 1,
			slidesToShow: 1,
			loop: true,
			infinite: true,
			autoplay: true,
			autoplaySpeed: 5000,
    }

		// Initialize all carousels except training set
    var carousels = bulmaCarousel.attach('.carousel:not(#train-carousel)', options);
    // Training set carousel: disable autoplay
    bulmaCarousel.attach('#train-carousel', Object.assign({}, options, { autoplay: false }));
	
    bulmaSlider.attach();

})

// Test cases carousel controls
function scrollTrack(btn, direction) {
    const wrapper = btn.closest('.carousel-wrapper');
    if (!wrapper) return;
    const track = wrapper.querySelector('.carousel-track');
    const item = track ? track.querySelector('.episode-card') : null;
    if (!track || !item) return;
    const scrollAmount = track.clientWidth || (item.offsetWidth + 20);
    track.scrollLeft += direction * scrollAmount;
}

function copyBibtex(button) {
    const content = document.getElementById('bibtex-content').innerText;
    navigator.clipboard.writeText(content).then(() => {
        const btnTextSpan = button.querySelector('.btn-text');
        button.classList.add('copied');
        btnTextSpan.innerText = 'Copied!';
        setTimeout(() => {
            button.classList.remove('copied');
            btnTextSpan.innerText = 'Copy';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}
// Fallback: delegate clicks in case inline handlers are blocked
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.carousel-wrapper .nav-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            const direction = btn.classList.contains('prev-btn') ? -1 : 1;
            scrollTrack(btn, direction);
        });
    });
});
