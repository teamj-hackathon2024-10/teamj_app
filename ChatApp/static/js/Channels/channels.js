//全てのモーダルトリガーとモーダルを取得
const modalTriggers = document.querySelectorAll("[data-modal-trigger]");
const modals = document.querySelectorAll("[data-modal]");

//モーダルを開く処理
modalTriggers.forEach(trigger => {
    trigger.addEventListener("click", (event) => {
        console.log("Trigger clicked:", trigger);
        const modalId = trigger.getAttribute("data-modal-trigger");
        console.log("Modal ID:", modalId);
        const targetModal = document.querySelector(`[data-modal="${modalId}"]`);

        if(targetModal){
            targetModal.style.display = "flex";
        }else{
            console.error(`モーダルが見つかりません：${modalId}`);
        }
    });
});

//モーダルを閉じる処理(背景クリック)
modals.forEach(modal => {
    modal.addEventListener("click", (e) => {
        if(e.target === modal){
        modal.style.display = "none"
        }
    });
});
