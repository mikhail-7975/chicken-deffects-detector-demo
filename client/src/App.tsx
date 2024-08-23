import React from "react";
import "./App.scss";
import { Tab } from "./components/Tab";
import { DescriptionBlock } from "./components/DescriptionBlock";

function App() {
  const checkDBUserExist = async () => {
    const response = await fetch("http://127.0.0.1:5000/post-example?id=2", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({"login":"login"})
    });
    return await response.json();
  };
  const testFunction = async () => {
    const response = await fetch("http://127.0.0.1:5000/?id=2",);
    return await response.json();
  };
  // testFunction();
  checkDBUserExist();
  return (
    <div className="App">
      <header className="App-header">Система сортировки куриных тушек</header>
      <main>
        <div className="navigationPanel">
          <div className="tabs" role="tablist">
            <Tab key="Statistics" title="Статистика" onClick={() => {}} />
            <Tab
              key="RealTimeView"
              title="Вид в реальном времени"
              isActive={true}
              onClick={() => {}}
            />
            <Tab
              key="Results"
              title="Результаты обнаружения"
              onClick={() => {}}
            />
          </div>
        </div>
        <div className="resultPanel">
          <div className="leftBlock">
            <div>
              <DescriptionBlock title="Передняя сторона голена слева" />
              <DescriptionBlock
                title="Бедро слева"
                type={"warning"}
                message={"Изменен цвет кожных покровов"}
              />
              <DescriptionBlock title="Грудка / задняя часть" />
              <DescriptionBlock title="Крыло слева" />
            </div>
            <div>
              <div className="resultBlock">
                <h3>Принятие решения по качеству</h3>
              </div>
            </div>
          </div>
          <div className="centerBlock">
            <h3>Вид в реальном времени</h3>
          </div>
          <div className="rightBlock">
            <DescriptionBlock title="Передняя сторона голена справа" />
            <DescriptionBlock title="Бедро справа" />
            <DescriptionBlock title="Целый" />
            <DescriptionBlock
              title="Крыло справа"
              type={"error"}
              message={"Сломана кость. Следы гематомы"}
            />
          </div>
        </div>
      </main>
      <footer>Все права защищены ©</footer>
    </div>
  );
}

export default App;
