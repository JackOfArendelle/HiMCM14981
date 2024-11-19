data2 = [14.444, 14.925, 15.132, 15.613, 15.751, 15.820, 15.888, 16.370, 16.439];  

data3 = [4.200, 4.215, 4.238, 4.245, 4.268, 4.313, 4.335, 4.350, 4.373];  

months = 1:9;  

p2 = polyfit(months, data2, 1);  

p3 = polyfit(months, data3, 1);  

new_data2_initial = 1.1; % 新的data2的初始值 

new_data3_initial = 1.031; % 新的data3的初始值 

new_p2 = [p2(1), new_data2_initial - p2(1)*1]; % 计算新的截距 

new_p3 = [p3(1), new_data3_initial - p3(1)*1]; % 计算新的截距 

months_full = 1:108;  

predicted_data2 = polyval(new_p2, months_full); 

predicted_data3 = polyval(new_p3, months_full);  

color2 = [165/225, 15/225, 21/225]; %#A50F15  

color3 = [100/225, 40/225, 70/225]; 

figure; 

hold on; 

plot(months_full, predicted_data2, 'LineWidth', 1, 'Color', color2);  

plot(months_full, predicted_data3, 'LineWidth', 1, 'Color', color3);  

hold off; 

legend('Swimming', 'Zwift Cycling', 'Location', 'Best'); 

title('Predicted Trends Index from 2024 to 2032', 'FontSize', 12); 

xlabel('Year', 'FontSize', 10); 

ylabel('Predicted Value', 'FontSize', 10); 

grid on; 

xticks(1:12:108);  

xticklabels(2024:2032);  

set(gca, 'FontSize', 10); 