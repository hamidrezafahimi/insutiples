clc
clear all
close all

files = ['position_2020-11-21-15-35-25.csv'; 'position_2020-11-21-18-32-28.csv';
         'position_2020-11-21-18-56-02.csv'; 'position_2020-11-21-19-13-39.csv';
         'position_2020-11-21-19-23-45.csv'; 'position_2020-11-21-19-34-25.csv';
         'position_2020-11-21-19-41-55.csv'; 'position_2020-11-21-19-45-02.csv';
         'position_2020-11-21-19-50-38.csv'; 'position_2020-11-21-19-57-03.csv'];

for i=1:10
    i
    d = csvread(files(i,:),1,0);
    x = 2*smoothdata(d(:,2),'movmedian',5);
    y = 2*smoothdata(d(:,3),'movmedian',5);
    z = smoothdata(d(:,4),'movmedian',5);
    
    text(x(1),y(1)-1,z(1), num2str(i),'HorizontalAlignment','left','FontSize',14,'FontName','Times New Roman');
    plot3(x,y,z,'--','LineWidth',1,'DisplayName',['Test ',num2str(i)]);
    hold on;
    grid on;
    
end

plot3([6.5,7.5,7.5,6.5,6.5],[-8.5,-8.5,-8.5,-8.5,-8.5],[9.5,9.5,8.5,8.5,9.5], 'color','red','LineWidth',3,'DisplayName','Window Boundaries');

xlabel('x [m]','FontSize',16,'FontName','Times New Roman') 
ylabel('y [m]','FontSize',16,'FontName','Times New Roman') 
zlabel('z [m]','FontSize',16,'FontName','Times New Roman')

legend('FontSize',12,'FontName','Times New Roman')
view([6,-5,5])
