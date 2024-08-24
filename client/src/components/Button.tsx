import React from "react";
import { Button as AntdButton, ButtonProps } from "antd";
import styles from "./Button.module.scss";

/**
 * Компонента кнопки без залипания
 */
export const Button = (props: Props) => {
  return (
    <AntdButton
      {...props}
      className={`${styles.Button} 
       ${props.type === "primary" ? styles.primary : ""} 
       ${props.danger ? styles.danger : ""} 
       ${props.color ? styles[props.color] : ""} 
       ${props.className ? props.className : ""}
       `}
      onMouseDown={(ev) => ev.preventDefault()}
    />
  );
};

type Props = Omit<ButtonProps, "color"> & {
  color?:
    | "black"
    | "black-light"
    | "success"
    | "success-light"
    | "primary-light"
    | "default"
    | "default-light"
    | "info"
    | "info-light"
    | "warning"
    | "warning-light"
    | "danger-light";
};
