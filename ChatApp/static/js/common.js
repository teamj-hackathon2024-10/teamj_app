const ham = document.querySelector('#js-hamburger'); //js-hamburgerの要素を取得し、変数hamに格納する
const nav = document.querySelector('#js-nav'); //js-navの要素を取得し、変数navに格納する

ham.addEventListener('click', function () { //ハンバーガーメニューをクリックしたら

  ham.classList.toggle('active'); // ハンバーガーメニューにactiveクラスを付け外しする
  nav.classList.toggle('active'); // ナビゲーションメニューにactiveクラスを付け外しする

});