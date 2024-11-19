data1 = [2.667, 2.676, 2.695, 2.752, 2.798, 2.845, 2.883, 2.921, 2.968];  

data2 = [14.444, 14.925, 15.132, 15.613, 15.751, 15.820, 15.888, 16.370,16.439];  

data3 = [4.200, 4.215, 4.238, 4.245, 4.268, 4.313, 4.335, 4.350, 4.373];  

months = 1:9;  

p1 = polyfit(months, data1, 1);  

p2 = polyfit(months, data2, 1);  

p3 = polyfit(months, data3, 1);  

% 预测2024年1月到2032年的数据（月份从1到108） 

months_full = 1:108;  

predicted_data1 = polyval(p1, months_full);  

predicted_data2 = polyval(p2, months_full); 

predicted_data3 = polyval(p3, months_full);  

color1 = [8/255, 81/255, 190/255]; % #08519C 

color2 = [20/225, 130/225, 160/225];  

color3 = [90/225, 105/225, 100/225]; 

figure; 

hold on; 

plot(months_full, predicted_data1, 'LineWidth', 1, 'Color', color1);  

plot(months_full, predicted_data2, 'LineWidth', 1, 'Color', color2);  

plot(months_full, predicted_data3, 'LineWidth', 1, 'Color', color3);  

hold off; 

legend('Australian Rule Football', 'Aquatics', 'Cycling', 'Location', 'Best'); 

title('Predicted Trends Index from 2024 to 2032', 'FontSize', 12); 

xlabel('Year', 'FontSize', 10); 

ylabel('Predicted Value', 'FontSize', 10); 

grid on; 

xticks(1:12:108);  

xticklabels(2024:2032);  

set(gca, 'FontSize', 10);  