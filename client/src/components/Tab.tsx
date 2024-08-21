import React from "react";
import styles from "./Tab.module.scss";

export const Tab = ({ key, title, onClick, isActive = false }: Props) => {
  return (
    <a
      className={`${styles.tabLink} ${isActive ? styles.active : ""}`}
      onClick={onClick}
      role="tab"
      data-testid={key}
      tabIndex={0}
    >
      {title}
    </a>
  );
};

type Props = {
  onClick: () => void;
  key: string;
  title: string;
  isActive?: boolean;
};
