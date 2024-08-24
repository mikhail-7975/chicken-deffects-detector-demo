import {
  BackwardOutlined,
  ForwardOutlined,
  PauseOutlined,
} from "@ant-design/icons";
import { Button } from "./Button";
import styles from "./ImagePanel.module.scss";
import { ImageType } from "../types";

export const ImagePanel = ({
  getNewImage,
  data,
  prevIsDisabled,
}: {
  getNewImage: (type: ImageType, enablePrevButton: boolean) => void;
  data: string;
  prevIsDisabled: boolean;
}) => {
  return (
    <>
      <div className={styles.imagePanel}>
        <img src={`data:image/jpeg;base64,${data}`} alt={"Куриная тушка"} />
        <div className={styles.controlPanel}>
          <Button
            type="primary"
            disabled={prevIsDisabled}
            icon={<BackwardOutlined />}
            onClick={() => getNewImage("previous", true)}
          >
            Предыдущее
          </Button>
          <Button danger icon={<PauseOutlined />}>
            Стоп
          </Button>
          <Button
            type="primary"
            icon={<ForwardOutlined />}
            onClick={() => getNewImage("next", true)}
          >
            Следующее
          </Button>
        </div>
      </div>
    </>
  );
};
