import { Alert, AlertProps } from "./Alert";
import React from "react";
import styles from "./DescriptionBlock.module.scss";

export const DescriptionBlock = ({
  title,
  type = "success",
  message = "OK",
}: Props) => {
  return (
    <div className={styles.block}>
      <h3>{title}</h3>
      <Alert type={type} message={message} />
    </div>
  );
};

type Props = {
  title: string;
  type?: AlertProps["type"];
  message?: string;
};
