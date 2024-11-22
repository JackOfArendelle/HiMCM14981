years = [2012, 2016, 2020, 2024]; 
data1 = [0.374553, 0.360505, 0.312229, 0.320517]; 
data2 = [0.508329, 0.464527, 0.422502, 0.453644];  
a1 = (max(data1) - min(data1)) / 2;  
a2 = (max(data2) - min(data2)) / 2;  
period = 5;  
b1 = 2 * pi / period;  
b2 = 2 * pi / period; 
c1 = 0;  
c2 = 0;  
d1 = mean(data1);  
d2 = mean(data2); 
StartPoint1 = [a1, b1, c1, d1];
StartPoint2 = [a2, b2, c2, d2];
ft1 = fittype('a*sin(b*x + c) + d', 'independent', 'x', 'dependent', 'y');
[fit1, gof1] = fit(years(:), data1(:), ft1, 'StartPoint', StartPoint1); 
ft2 = fittype('a*sin(b*x + c) + d', 'independent', 'x', 'dependent', 'y');
[fit2, gof2] = fit(years(:), data2(:), ft2, 'StartPoint', StartPoint2); 
year_full = linspace(min(years), max(years), 1000);  
trend1 = feval(fit1, year_full);
trend2 = feval(fit2, year_full);
predict_2032_data1 = feval(fit1, 2032);
predict_2032_data2 = feval(fit2, 2032);

figure;

% 第一张子图 - Disciplines
subplot(1, 2, 1);
hold on;
plot(years, data1, 'ko', 'MarkerSize', 6, 'DisplayName', 'Disciplines Raw Data');  
plot(year_full, trend1, 'b-', 'DisplayName', 'Disciplines Predicted Score Limit', 'LineWidth', 2);  
text(2024, predict_2032_data1, ['2032: ' num2str(predict_2032_data1, '%.3f')], 'Color', 'blue', 'FontSize', 10);  
legend('show');
title('Disciplines Predicted Score Limit');
xlabel('Year');
ylabel('Score Value');

% 第二张子图 - Sports
subplot(1, 2, 2);
hold on;
plot(years, data2, 'ks', 'MarkerSize', 6, 'DisplayName', 'Sports Raw Data');  
plot(year_full, trend2, 'r-', 'DisplayName', 'Sports Predicted Score Limit', 'LineWidth', 2);
text(2024, predict_2032_data2, ['2032: ' num2str(predict_2032_data2, '%.3f')], 'Color', 'red', 'FontSize', 10);  
legend('show');
title('Sports Predicted Score Limit');
xlabel('Year');
ylabel('Score Value');