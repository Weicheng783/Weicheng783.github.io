
<html>
    <head>
        <link rel="icon" type="image/x-icon" href="./favicon.ico" />
        <meta charset="utf-8">
        <title>Weicheng Space</title>
        <meta name="author" content="Weicheng Ao">
        <meta name="revised" content="Weicheng Ao, Canary Edition 11/30/2021">
    </head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />


    <body style="background-color: antiquewhite;">
        <!-- <div id="header_group" > -->
          <div id='header_group' style="display:block; text-align: center;">
            <div style="display: inline-flex;">
            <img src="./logo.png" id="logo" alt="Weicheng_Space_Welcome_Message" style=" text-align: left; border-radius:20px; display:inline-block; height:100px; width:auto;">
            </div>

            <!-- 连接中心数据库 -->
            <?php
                header("Content-type:text/html;charset=utf-8");
                // $con = mysqli_connect("localhost:872","root","");
                // if (!$con){
                //     echo "<h3 style='text-align:center; color:red;'>中心数据库连接失败。目前离线查看。</h3>";
                //     die('中心数据库连接失败' . mysql_error());
                // }else{
                //     echo "<h3 style='text-align:center; color:green;'>中心数据库连接成功。</h3>";
                // }

                $dsn="mysql:host=localhost";
                $user="root";
                $password='';
                try
                {
                    $pdo=new PDO($dsn,$user,$password);
                    $pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
                    echo "<h3 style='text-align:center; color:green;'>中心数据库连接成功。</h3>";
                    // echo '<img src="./today.jpg"  alt="Let us see your future." style=" text-align: left; border-radius:20px; display:inline-block; height:auto; width:80%;">
                    // ';
                }
                catch(PDOException $e)
                {
                    echo "<h3 style='text-align:center; color:red;'>中心数据库连接失败。目前离线查看。</h3>";
                    echo $e->getMessage();
                }

                $pdo=new PDO($dsn,$user,$password);
                $pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);

                $sql = "CREATE DATABASE IF NOT EXISTS thoughtsdb";
                $pdo->query($sql);
                $sql = "CREATE TABLE IF NOT EXISTS feeds
                (
                    feedsid INT (11) UNSIGNED not null AUTO_INCREMENT,
                    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP(),
                    editor VARCHAR(10) not null DEFAULT 'Harvey Ao',
                    message TEXT(65535),
                    photo_addresses TEXT(65535),
                    comments TEXT(65535),

                    PRIMARY KEY (feedsid)
                )";

                $pdo = new pdo('mysql:host=localhost; dbname=thoughtsdb', 'root', '');
                $pdo->query($sql);

                // function diaryData(){
                //     $diary['']
                // }



            ?>

            <p class="narrator" style="font-size: x-large; text-align: center; " id="ymd"></p>
            <div style="text-align: center;">
            <button type="button" class="header_button" onclick="convert();">Today</button>
            <button type="button" class="header_button" onclick="convert();">My Card</button>
            
            <button type="button" class="header_button" onclick="location.href='/phpmyadmin'">Php My Admin</button>
            </div>
                <form action="upLoadtofilesystem.php" method="post" style="display:center;">
                    <!-- <input type="hidden" name="res1" id="res1_id"/> -->
                    <!-- <input type="hidden" name="res2" id="res2_id"/> -->
                    <!-- <input type="input" name="flag" id="flagg_id"/> -->
                    <!-- <button type="submit" class="header_button" onclick="new_task()">New Task</button> -->
                    <button type="submit" class="header_button" onclick="">Post Now!</button>
                </form>
           </div>

            <div style="text-align: center;">
                <!-- <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=1422432288&auto=1&height=66"></iframe> -->
                <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=490595480&auto=1&height=66"></iframe>
            </div>

            <div id="writingArea" style="text-align:center; border-style:dashed; border-width:3px; border-radius:5px; padding:5px; margin:5px;">
                <form action="uploadtoDB.php" method="post" style="display:center;">
                    <p>Editor: <input name="editor"></input></p>
                    <p>Message: <textarea name="message" style="font-style:italic;"></textarea></p>
                    <p>Photos Address: <input name="photos"></input></p>
                    <p>Comments: <textarea name="comments"></textarea></p>
                    <p><button type="submit" class="header_button" onclick="upLoadtofileSystem();">Post Now!</button></p>
                </form>
            </div>


            <!-- 中心数据库取回数据 -->
            <?php
                $stmt = $pdo->query('select * from feeds');
                 //从结果集中获取下一行，用于while循环
                // $rows = $stmt->fetchAll(); //获取所有
                $row_count = $stmt->rowCount();
                $rows = $stmt->fetchAll();

                for($i = $row_count-1; $i >= 0; $i--){
                    
                    echo '<div class="message" style="text-align:center; border-style:solid; border-width:3px; border-radius:5px; padding:5px; margin:5px;">';
                    if($rows[$i]['editor'] != NULL){
                        echo '<p id="editor">'.$rows[$i]['editor'].'</p>';
                    }
                    echo '<p id="time">'.$rows[$i]['time'].'</p>';
                    if($rows[$i]['message'] != NULL){
                        echo '<p id="message">'.$rows[$i]['message'].'</p>';
                    }
                    if($rows[$i]['photo_addresses'] != NULL){
                        echo '<p id="photos">'.$rows[$i]['photo_addresses'].'</p>';
                    }
                    if($rows[$i]['comments'] != NULL){
                        echo '<p id="comments">'.$rows[$i]['comments'].'</p>';
                    }

                    echo '</div>';
                }

                // print_r($rows);
            
            ?>


    </body>

</html>

<script>

function fun(){
        var date = new Date()
        var y = date.getFullYear();
        var m = date.getMonth()+1;
        var d = date.getDate(); 
        var hh = date.getHours();
        var mm = date.getMinutes();
        var ss = date.getSeconds();
        if(hh <= 6 & hh >= 0){
            var notice = "夜深了，但新的一天开始啦~ 凌晨时分，快些睡觉吧!"
        }else if(hh > 6 & hh < 11){
            var notice = "上午开始啦！抓住大好时光，去做事情吧！"
        }else if(hh >= 11  & hh <= 12){
            var notice = "午间时分咯~ 注意快些结束事情，准备干饭吧！"
        }else if(hh > 12 & hh <= 18){
            var notice = "下午开始啦！抓住大好时光，去做事情吧！"
        }else if(hh >= 19 & hh <= 22){
            var notice = "晚上了~ 这段时间应该好好安排一下咯~"
        }else if(hh > 22 & hh <= 23){
            var notice = "夜深了，差不多收拾一下，准备休息吧。"
        }else{
            var notice = "继续加油哦~"
        }

        document.getElementById("ymd").innerHTML = +y+"-"+m+"-"+d+" "+hh+":"+mm+":"+ss+" "+notice+"我的伙伴。";
        setTimeout("fun()",1000)
    }




    window.onload = function(){
        setTimeout("fun()",0)
    }
</script>


<style>
    .narrator{
        animation-name: narrator_enter; 
        animation-duration:5s;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }

    @keyframes narrator_enter {
        0%   {margin-top:-50px;}
        100% {margin-top:15px;}
    }

    #logo{
        text-align:left;
    }

    #header {
        
        /* display: inline-block; */
        border-radius: 5px;
        border-width: 5px;
        border: solid;
        border-color: skyblue;
        background-color: antiquewhite;
        text-align: center;
        display:inline-block;
        margin-left: 25%;
        /* margin-right: 50%; */
        
    }

    .header_button {
        margin: 20px, 20px, 20px, 20px;
        border-radius: 10px;
        /* text-align: right; */

        font-size: large;
    }

    .header_button:hover{
        background-color: rgb(36, 200, 221);
    }

    .header_button:active{
        background-color: sandybrown;
    }

    .good{
        text-align: center;    
    }

</style>
