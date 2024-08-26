import React from "react";
import { Button as AntdButton, ButtonProps } from "antd";
import styles from "./Button.module.scss";

export const Button = (props: Props) => {
  return (
    <AntdButton
      {...props}
      className={`${styles.Button} 
       ${props.type === "primary" ? styles.primary : ""} 
       ${props.danger ? styles.danger : ""} 
       ${props.disabled ? styles.default : ""} 
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
    | "primary-light"
    | "default"
    | "default-light"
    | "danger-light";
};
