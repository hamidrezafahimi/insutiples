void setWindow(Mat im){

  // Point win_ca;
  namedWindow("operator desicion");
  setMouseCallback( "operator desicion", onMouse, 0 );
  imshow("operator desicion", frm);
  waitKey();
  return;
}
