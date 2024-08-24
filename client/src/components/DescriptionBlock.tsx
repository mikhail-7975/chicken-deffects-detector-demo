import { Alert } from "./Alert";
import React from "react";
import styles from "./DescriptionBlock.module.scss";
import { AlertProps, DetectionInfo } from "../types";

export const DescriptionAlert = ({
  type = "success",
  message = "Дефектов нет",
}: DescriptionAlertProps) => {
  return <Alert type={type} message={message} />;
};

export const DescriptionBlock = ({
  title,
  defectsDescription,
}: {
  title: string;
  defectsDescription: DetectionInfo[];
}) => {
  return (
    <div className={styles.block}>
      <h3>{title}</h3>
      {defectsDescription.length === 0 ? (
        <DescriptionAlert type={"info"} message={"Нет данных"} />
      ) : (
        defectsDescription.map((defect) => {
          return (
            <DescriptionAlert
              type={
                defect.color === "yellow"
                  ? "warning"
                  : defect.color === "red"
                    ? "error"
                    : "success"
              }
              message={defect.message}
            />
          );
        })
      )}
    </div>
  );
};

type DescriptionAlertProps = {
  type?: AlertProps["type"];
  message?: string;
};
