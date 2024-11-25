//全てのモーダルトリガーとモーダルを取得
const modalTriggers = document.querySelectorAll("[data-modal-trigger]");
const modals = document.querySelectorAll("[data-modal]");

//モーダルを開く処理
modalTriggers.forEach(trigger => {
    trigger.addEventListener("click", (event) => {
        console.log("Trigger clicked:", trigger);
        const modalId = trigger.getAttribute("data-modal-trigger");
        console.log("Modal ID:", modalId);

        openModal(modalId);
    });
});


//モーダル表示用関数
function openModal(modalId){
    const targetModal = document.querySelector(`[data-modal="${modalId}"]`);
    if(targetModal){
        targetModal.style.display = "flex";//モーダルを表示
    }else{
        console.error(`モーダルが見つかりません：${modalId}`);
    }
}


//モーダルを閉じる処理(背景クリック)
modals.forEach(modal => {
    modal.addEventListener("click", (e) => {
        if(e.target === modal){
        modal.style.display = "none"
        }
    });
});


//チャンネル登録フォーム送信時の処理
document.getElementById(`add-channel-form`).addEventListener(`submit`,function(event){
    event.preventDefault(); //フォーム送信を防ぐ(ページが遷移しないように)

    //入力したチャンネル名を取得
    const channelName = document.getElementById('add-channel-input-value').value;
    console.log("チャンネル名を取得できました。", channelName);
    
    //チャンネル名を確認モーダルに表示
    const addChannelDisplay = document.getElementById("add-channel-display");
    addChannelDisplay.value = channelName;
    addChannelDisplay.setAttribute("readonly",true);
    console.log(addChannelDisplay);

    //確認モーダルを表示
    openModal(`add-channel-confirmation-modal`);
});


// 戻るリンクをクリックしたときの処理(チャンネル追加)
document.getElementById('back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.querySelector('[data-modal="add-channel-confirmation-modal"]').style.display = "none";
});


//チャンネル編集フォーム送信時の処理
document.getElementById(`update-channel-form`).addEventListener(`submit`,function(event){
    event.preventDefault(); //フォーム送信を防ぐ(ページが遷移しないように)

    //入力したチャンネル名を取得
    const channelName = document.getElementById(`update-channel-input-value`).value;
    console.log("チャンネル名取得：",channelName);
    //チャンネル名を確認モーダルに表示
    const updateChannelDisplay = document.getElementById("update-channel-display");
    updateChannelDisplay.value = channelName;
    updateChannelDisplay.setAttribute("readonly",true);
    console.log("編集チャンネル名：",updateChannelDisplay);

    //チェックされたメンバーを取得
    const checkboxes = document.querySelectorAll(`.add-member-checkbox input[type="checkbox"]`);
    const selectedMembers = Array.from(checkboxes).filter(checkbox => checkbox.checked)//チェックされた要素を取得
    .map(checkbox => checkbox.parentElement.textContent.trim()); //ラベルのテキストを取得

    console.log("選択されたメンバー:",selectedMembers);

    //選択されたメンバーを確認モーダルに表示
    const selectedMembersDisplay = document.getElementById("hidden-selected-members");
    selectedMembersDisplay.innerHTML = selectedMembers.length > 0 
        ? selectedMembers.join("<br>") : "選択されたメンバーはいません";

    //サーバー送信用の隠しフィールドにも設定
    const hiddenSelectedMembers = document.getElementById("hidden-selected-members");
    hiddenSelectedMembers.value = selectedMembers.join(","); //カンマ区切りで送信

    openModal(`update-channel-confirmation-modal`);
});


// 戻るリンクをクリックしたときの処理(チャンネル編集)
document.getElementById('back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.querySelector('[data-modal="update-channel-confirmation-modal"]').style.display = "none";
});


//チャンネル削除フォーム送信時の処理
document.getElementById(`delete-channel-form`).addEventListener(`submit`,function(event){
    event.preventDefault(); //フォーム送信を防ぐ(ページが遷移しないように)

    //確認モーダルを表示
    openModal(`delete-channel-confirmation-modal`);
});


