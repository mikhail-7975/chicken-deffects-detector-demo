import React from "react";
import { render, screen } from "@testing-library/react";
import App from "../src/App";

test("renders main page", () => {
  render(<App />);
  const headerElement = screen.getByText(/Система сортировки куриных тушек/i);
  expect(headerElement).toBeInTheDocument();
});
