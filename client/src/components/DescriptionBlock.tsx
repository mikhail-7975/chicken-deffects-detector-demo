import { Alert } from "./Alert";
import React from "react";
import styles from "./DescriptionBlock.module.scss";
import { AlertProps, DetectionInfo } from "../types";
import { Skeleton } from "antd";

export const DescriptionAlert = ({
  type = "success",
  message = "Дефекты не обнаружены",
}: DescriptionAlertProps) => {
  return <Alert type={type} message={message} />;
};

export const DescriptionBlock = ({
  title,
  defectsDescription,
  isLoading = false,
}: {
  title: string;
  defectsDescription: DetectionInfo[];
  isLoading: boolean;
}) => {
  return (
    <div className={styles.block}>
      <h3>{title}</h3>
      {isLoading ? (
        <Skeleton active />
      ) : defectsDescription.length === 0 ? (
        <DescriptionAlert type={"info"} message={"Дефекты не обнаружены"} />
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
