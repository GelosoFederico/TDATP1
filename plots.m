clear all
close all

A = csvread('Running_time.csv');
loglog(A(1,2:end),A(2,2:end),'bo-')
hold on
loglog(A(1,1:6),A(3,1:6),'ro-')

Hleg=legend('E','F','Location','southeast');
legend('boxon');
set(Hleg,'FontName','Arial','FontSize',10);

title('Tiempos de corridas','Fontsize',11)
xlabel('n')
ylabel('T [s]')

grid minor
axis([10 10^10 10^-3 1000])
print('Tiempos_corridas.png','-dpng');
