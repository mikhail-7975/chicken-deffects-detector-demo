import React, { useEffect, useState } from "react";
import "./App.scss";
import { Tab } from "./components/Tab";
import { DescriptionBlock } from "./components/DescriptionBlock";
import { ImagePanel } from "./components/ImagePanel";
import { getDefaultImage, getImage } from "./api";
import { DetectedImage, ImageType } from "./types";
import { Input, Skeleton, Spin } from "antd";
import { LoadingOutlined } from "@ant-design/icons";
import { Alert } from "./components/Alert";

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
  const [error, setError] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [prevIsDisabled, setPrevIsDisabled] = useState<boolean>(true);

  const getNewImage = (type: ImageType, enablePrevButton: boolean) => {
    setIsLoading(true);
    setError("");
    getImage(type)
      .then((res: DetectedImage) => {
        setDetectedImage(res);
        if (type === "next" && enablePrevButton) setPrevIsDisabled(false);
      })
      .catch((e) => setError(e.message || "Произошла ошибка. Попробуйте снова"))
      .finally(() => setIsLoading(false));
  };

  useEffect(() => {
    setIsLoading(true);
    setError("");
    getDefaultImage()
      .then((res: DetectedImage) => {
        setDetectedImage(res);
      })
      .catch((e) => setError(e.message || "Произошла ошибка. Попробуйте снова"))
      .finally(() => setIsLoading(false));
  }, []);

  // useEffect(() => {
  //   getNewImage("next", false);
  // }, []);

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
                isLoading={isLoading || !!error}
              />
              <DescriptionBlock
                title="Грудка / задняя часть"
                defectsDescription={[]}
                isLoading={isLoading || !!error}
              />
              <DescriptionBlock
                title="Крыло слева"
                defectsDescription={detectedImage.left_wing}
                isLoading={isLoading || !!error}
              />
            </div>
            <div>
              <div className="resultBlock">
                <h3>Принятие решения по качеству</h3>
                {isLoading || !!error ? (
                  <Skeleton active />
                ) : (
                  <Input value={detectedImage.decision} disabled />
                )}
              </div>
            </div>
          </div>
          <div className="centerBlock">
            <h3>Вид в реальном времени</h3>
            {isLoading ? (
              <div style={{ marginTop: "30px" }}>
                <Spin
                  indicator={<LoadingOutlined style={{ fontSize: 24 }} spin />}
                />
              </div>
            ) : !!error ? (
              <Alert type={"error"} message={error} />
            ) : (
              detectedImage.image && (
                <ImagePanel
                  getNewImage={getNewImage}
                  data={detectedImage.image}
                  prevIsDisabled={prevIsDisabled}
                />
              )
            )}
          </div>
          <div className="rightBlock">
            <DescriptionBlock
              title="Ножка справа"
              defectsDescription={detectedImage.right_leg}
              isLoading={isLoading || !!error}
            />
            <DescriptionBlock
              title="Целый"
              defectsDescription={detectedImage.body}
              isLoading={isLoading || !!error}
            />
            <DescriptionBlock
              title="Крыло справа"
              defectsDescription={detectedImage.right_wing}
              isLoading={isLoading || !!error}
            />
          </div>
        </div>
      </main>
      <footer>Все права защищены ©</footer>
    </div>
  );
}

export default App;
