import React from "react";
import { Alert as AntdAlert } from "antd";
import styles from "./Alert.module.scss";
import { AlertProps } from "../types";

export const Alert = (props: AlertProps) => (
  <AntdAlert
    {...props}
    className={`${styles.alert} ${props.className ?? ""}`}
  />
);
