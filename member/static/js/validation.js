// 회원가입 유효성 검사
function checkMember(){
    let form = document.regForm;
    let id = form.memberid;
    let pw1 = form.passwd1;
    let pw2 = form.passwd2;


    if(id.value.length < 4 || id.value.length > 15){
        alert("아이디는 4~15자까지 입력 가능합니다.");
        id.select();
        return false;
    }else if(pw1.value.length < 8){
        alert("비밀번호는 영문자/숫자/특수문자 포함 8자 이상 입력해주세요.");
        id.select();
        return false;
    }


}