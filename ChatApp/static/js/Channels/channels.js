//新規登録ボタン押下時処理

//新規チャンネル追加モーダル
const addChannelModal = document.getElementById("add-channel-modal");
//新規チャンネル追加確認モーダル
const addChannelModalConfirmation = document.getElementById("add-channel-confirmation-modal");

//新規チャンネル追加モーダル表示
document.getElementById("add-channel-button").addEventListener('click',function(event){
    console.log(addChannelModal);
    if(addChannelModal){
    addChannelModal.style.display = "flex"; //モーダルの表示
    }else{
        console.error("モーダルが見つかりません：",addChannelModal);
    }
});

//モーダルを閉じる処理(新規チャンネル追加)
addChannelModal.addEventListener("click", function(e){
    if(e.target === addChannelModal){
        addChannelModal.style.display = "none";
    }
});

//チャンネル追加確認モーダル表示
document.getElementById("add-channel-form").addEventListener("submit",function(event){
    event.preventDefault(); //フォーム送信を行わないようにするため。

    //入力したチャンネル名を取得
    const channelName = document.getElementById('add-channel-input-value').value;
    console.log(channelName);

    //チャンネル名を確認モーダルに表示
    const addChannelDisplay = document.getElementById("add-channel-display");
    console.log(addChannelDisplay);
    addChannelDisplay.value = channelName;
    addChannelDisplay.setAttribute("readonly",true);
    

    //確認モーダルを表示
    if(addChannelModalConfirmation){
        addChannelModalConfirmation.style.display = "flex";
    }else{
        console.error("確認画面のモーダルが見つかりません：",addChannelModalConfirmation);
    }
});

//モーダルを閉じる処理(新規チャンネル追加確認)
addChannelModalConfirmation.addEventListener("click", function(e){
    if(e.target === addChannelModalConfirmation){
        addChannelModalConfirmation.style.display = "none";
    }
});

// 戻るリンクをクリックしたときの処理(チャンネル追加)
document.getElementById('add-back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.getElementById("add-channel-confirmation-modal").style.display = "none";
});


//チャンネル編集ボタン押下時処理

//チャンネル編集追加モーダル
const updateChannelModal = document.getElementById("update-channel-modal");
//チャンネル編集確認モーダル
const updateChannelModalConfirmation = document.getElementById("update-channel-confirmation-modal");

//channelsにDBから取得するデータを確保する。
//const channel

/*
//管理者かどうかを判定するフラグ
const isAdmin = true;

//channel.htmlに動的に作成したチャンネルデータを作成して挿入
//挿入元の親コンテナを取得
const channelsContainer = document.getElementById("channels-container");

//チャンネルリストを動的に作成
channels.forEach((channel, index) => {
    //チャンネル要素の作成
    const channelDiv = document.createElement("div");
    channelDiv.className = "channel";
    channelDiv.id = `channel-${channel.channel_id}`;

    //チャンネル名リンクの作成
    const channelLink = document.createElement("a");
    channelLink.className = "channel-name";
    channelLink.href = `/detail/${channel.channel_id}`;
    channelLink.textContent = channel.name;
    channelLink.id = `channel-name-${channel.channel_id}`;

    //管理者機能ボタンの追加
    if(isAdmin){
        //編集ボタン
        const editButton = document.createElement("i");
        editButton.className = "fa-solid fa-pen";
        editButton.id = `edit-channel-${channel.channel_id}`;
        
        //削除ボタン
        const deleteButton = document.createElement("i");
        deleteButton.className = "fa-solid fa-trash";
        deleteButton.id = `delete-channel-${channel.channel_id}`

        //ボタンをチャンネル要素に追加
        channelDiv.appendChild(editButton);
        channelDiv.appendChild(deleteButton);
    }

    //名前リンクをチャンネル要素に追加
    channelDiv.appendChild(channelLink);

    //完成したチャンネル要素を親コンテナに追加
    channelsContainer.appendChild(channelDiv);
});

*/
//チャンネル編集モーダル表示
document.getElementById("update-channel-button").addEventListener('click',function(event){

    // //編集対象のチャンネル名取得
    // const targetChannelName = document.getElementById("updated-channel-name").value;

    // //チャンネル編集モーダルに表示
    // const updateChannelDisplay = document.getElementById("update-channel-dispaly");
    // updateChannelDisplay.value = targetChannelName; 
    // updateChannelDisplay.setAttribute("readonly",true);

    //上記の処理はチャンネル一覧を取得する際にliタグで各チャンネルの要素を作成する必要があるので、その処理を作成した後に対応する。

    console.log(updateChannelModal);
    if(updateChannelModal){
    updateChannelModal.style.display = "flex"; //モーダルの表示
    }else{
        console.error("モーダルが見つかりません：",updateChannelModal);
    }
});


//モーダルを閉じる処理(新規チャンネル追加)
updateChannelModal.addEventListener("click", function(e){
    if(e.target === updateChannelModal){
        updateChannelModal.style.display = "none";
    }
});


//チャンネル編集確認モーダル表示
document.getElementById("update-channel-form").addEventListener("submit",function(event){
    event.preventDefault(); //フォーム送信を行わないようにするため。

    //入力したチャンネル名を取得
    const channelName = document.getElementById('update-channel-input-value').value;
    console.log(channelName);

    //チャンネル名を確認モーダルに表示
    const updateChannelDisplay = document.getElementById("update-channel-display");
    console.log(updateChannelDisplay);
    updateChannelDisplay.value = channelName;
    updateChannelDisplay.setAttribute("readonly",true);
    

    //確認モーダルを表示
    if(updateChannelModalConfirmation){
        updateChannelModalConfirmation.style.display = "flex";
    }else{
        console.error("確認画面のモーダルが見つかりません：",updateChannelModalConfirmation);
    }
});

//モーダルを閉じる処理(チャンネル編集確認)
updateChannelModalConfirmation.addEventListener("click", function(e){
    if(e.target === updateChannelModalConfirmation){
        updateChannelModalConfirmation.style.display = "none";
    }
});

// 戻るリンクをクリックしたときの処理(チャンネル編集)
document.getElementById('update-back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.getElementById("update-channel-confirmation-modal").style.display = "none";
});


//チャンネル削除ボタン押下時処理

//チャンネル削除モーダル
const deleteChannelModal = document.getElementById("delete-channel-modal");
//チャンネル削除確認モーダル
const deleteChannelModalConfirmation = document.getElementById("delete-channel-confirmation-modal");

//チャンネル削除モーダル表示
document.getElementById("delete-channel-button").addEventListener('click',function(event){
    console.log(deleteChannelModal);
    if(deleteChannelModal){
    deleteChannelModal.style.display = "flex"; //モーダルの表示
    }else{
        console.error("モーダルが見つかりません：", deleteChannelModal);
    }
    console.log(deleteChannelModalConfirmation);
});

//モーダルを閉じる処理(チャンネル削除)
deleteChannelModal.addEventListener("click", function(e){
    if(e.target === deleteChannelModal){
        deleteChannelModal.style.display = "none";
    }
});

//チャンネル削除確認モーダル表示
document.getElementById("delete-channel-form").addEventListener("submit",function(event){
    event.preventDefault(); //フォーム送信を行わないようにするため。
    //削除対象チャンネル名を取得
    const channelName = document.getElementById('delete-channel-input-value').value;
    console.log(channelName);

    //チャンネル名を確認モーダルに表示
    const deleteChannelDisplay = document.getElementById("delete-channel-display");
    console.log(deleteChannelDisplay);
    deleteChannelDisplay.value = channelName;
    deleteChannelDisplay.setAttribute("readonly",true);
    

    console.log("削除確認モーダル表示：",deleteChannelModalConfirmation);

    //確認モーダルを表示
    if(deleteChannelModalConfirmation){
        deleteChannelModalConfirmation.style.display = "flex";
    }else{
        console.error("確認画面のモーダルが見つかりません：",deleteChannelModalConfirmation);
    }
});

//モーダルを閉じる処理(新規チャンネル追加確認)
deleteChannelModalConfirmation.addEventListener("click", function(e){
    if(e.target === deleteChannelModalConfirmation){
        deleteChannelModalConfirmation.style.display = "none";
    }
});

// 戻るリンクをクリックしたときの処理(チャンネル削除)
document.getElementById('delete-back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.getElementById("delete-channel-confirmation-modal").style.display = "none";
});