@startuml
title AIによる改善提案フローのシーケンス

actor User
participant "FlowEditor (Component)" as Editor
participant "mockAI (Util)" as MockAI
participant "useFlowData (Hook)" as FlowHook
database "LocalStorage" as LS

User -> Editor : 「AI改善提案」ボタンをクリック
activate Editor

Editor -> MockAI : improveProcess(asIsCode)
activate MockAI
MockAI -> MockAI : 改善提案とTo-Beコードを生成
MockAI --> Editor : { suggestions, toBeCode, ... } を返す
deactivate MockAI

Editor -> Editor : 内部Stateを更新 (To-Be, 改善効果など)
note right of Editor : 画面に改善提案と\nTo-Beの図が表示される

Editor -> FlowHook : updateFlowData(flowId, newData)
activate FlowHook
FlowHook -> LS : As-IsとTo-Beの両方を含む\n新しいフローデータを保存
deactivate FlowHook

deactivate Editor

@enduml