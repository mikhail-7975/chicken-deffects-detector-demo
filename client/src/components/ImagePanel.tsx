import {
  BackwardOutlined,
  ForwardOutlined,
  PauseOutlined,
} from "@ant-design/icons";
import { Button } from "./Button";
import { useState } from "react";
import styles from "./ImagePanel.module.scss";
import { ImageType } from "../types";

export const ImagePanel = ({
  getNewImage,
}: {
  getNewImage: (type: ImageType) => void;
}) => {
  const [image, setImage] = useState<{ name: string; path: string }>();
  return (
    <>
      <div className={styles.imagePanel}>
        <img src={image?.path} alt={image?.name} />
        <div className={styles.controlPanel}>
          <Button
            type="primary"
            // disabled
            icon={<BackwardOutlined />}
            onClick={() => getNewImage("previous")}
          >
            Предыдущее
          </Button>
          <Button danger icon={<PauseOutlined />}>
            Стоп
          </Button>
          <Button
            type="primary"
            // disabled
            icon={<ForwardOutlined />}
            onClick={() => getNewImage("next")}
          >
            Следующее
          </Button>
        </div>
      </div>
    </>
  );
};
