import React from "react";
import { AlertProps as AntdAlertProps, Alert as AntdAlert } from "antd";
import styles from "./Alert.module.scss";

export const Alert = (props: AlertProps) => (
  <AntdAlert
    {...props}
    className={`${styles.alert} ${props.className ?? ""}`}
  />
);

export type AlertProps = Omit<AntdAlertProps, "type"> & {
  type: "success" | "warning" | "error";
};
