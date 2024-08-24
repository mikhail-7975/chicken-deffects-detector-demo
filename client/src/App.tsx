import React, { useEffect, useState } from "react";
import "./App.scss";
import { Tab } from "./components/Tab";
import { DescriptionBlock } from "./components/DescriptionBlock";
import { ImagePanel } from "./components/ImagePanel";
import { getDefaultImage, getImage } from "./api";
import { DetectedImage, ImageType } from "./types";
import { Input } from "antd";

function App() {
  const [detectedImage, setDetectedImage] = useState<DetectedImage>({
    body: [],
    back: [],
    left_leg: [],
    right_leg: [],
    left_wing: [],
    right_wing: [],
    decision: "",
  });
  const getNewImage = (type: ImageType) => {
    getImage(type)
      .then((res: DetectedImage) => {
        setDetectedImage(res);
      })
      .catch();
  };
  useEffect(() => {
    getImage("next")
      .then((res: DetectedImage) => {
        setDetectedImage(res);
      })
      .catch();
  }, []);
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
              <DescriptionBlock
                title="Ножка слева"
                defectsDescription={detectedImage.left_leg}
              />
              <DescriptionBlock
                title="Грудка / задняя часть"
                defectsDescription={[]}
              />
              <DescriptionBlock
                title="Крыло слева"
                defectsDescription={detectedImage.left_wing}
              />
            </div>
            <div>
              <div className="resultBlock">
                <h3>Принятие решения по качеству</h3>
                <Input value={detectedImage.decision} disabled />
              </div>
            </div>
          </div>
          <div className="centerBlock">
            <h3>Вид в реальном времени</h3>
            <ImagePanel getNewImage={getNewImage} />
          </div>
          <div className="rightBlock">
            <DescriptionBlock
              title="Ножка справа"
              defectsDescription={detectedImage.right_leg}
            />
            <DescriptionBlock
              title="Целый"
              defectsDescription={detectedImage.body}
            />
            <DescriptionBlock
              title="Крыло справа"
              defectsDescription={detectedImage.right_wing}
            />
          </div>
        </div>
      </main>
      <footer>Все права защищены ©</footer>
    </div>
  );
}

export default App;
