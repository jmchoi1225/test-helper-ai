import React from 'react'
import Todolist from './Todolist'

function TestStudentIdentification(){
  return(
    <div className="m-5 p-5"> 
      <Todo ></Todo>
    </div>
  )
}
function Todo(){
  let pagetitle="TestStudentIdentification"
  let todos=["모바일로 접속된 화상회의화면에서 학생증을 캡쳐한다.","모바일로 접속된 화상회의화면에서 본인얼굴을 캡쳐한다.","학생증과 본인얼굴 사진이 AWS S3에 업로드 되는지 확인한다.","Flask와 AWS Rekognition을 통해 반환된 본인일치 결과를 보여준다."]
  let names=["승현","승현","승현","승현"]
  let dates=["","","",""]
  let status=["To do","To do","To do","To do"]
  return(
    <Todolist pagetitle={pagetitle} todos={todos} names={names} dates={dates} status={status} ></Todolist>
  )
}
export default TestStudentIdentification