import { AlertProps as AntdAlertProps } from "antd";

// export type res = {
//   image?: string;
//   body: Alert[]; //целый
//   back: Alert[]; //грудка и задняя часть
//   left_leg: Alert[]; //голень слева
//   right_leg: Alert[]; //голень справа
//   left_wing: Alert[]; //крыло слева
//   right_wing: Alert[]; //крыло справа
//   decision: string;
// };

// type Alert = AlertProps;

export type AlertProps = Omit<AntdAlertProps, "type"> & {
  type: "success" | "warning" | "error" | "info";
};

export type ImageType = "next" | "previous";

export type DetectedImage = {
  image?: string;
  body: DetectionInfo[]; //целый
  back: DetectionInfo[]; //грудка и задняя часть
  left_leg: DetectionInfo[]; //голень слева
  right_leg: DetectionInfo[]; //голень справа
  left_wing: DetectionInfo[]; //крыло слева
  right_wing: DetectionInfo[]; //крыло справа
  decision: string;
};

export type DetectionInfo = {
  defect_type: string;
  message: string;
  color: "yellow" | "red";
};
