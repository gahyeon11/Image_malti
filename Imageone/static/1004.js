fetch('/get-object-images')
    .then(response => response.json())
    .then(data => {
        data.object_images.forEach((obj, index) => {
            const img = new Image();
            img.src = obj.url;

            img.onload = () => {
                objectImages.push(img);
                objectPositions.push({ x: 0, y: 0, width: 100, height: 100 });
                drawImages();
            };
        });
    })
    .catch(error => console.error('Error:', error));



// 키보드 이벤트 처리
window.addEventListener('keydown', function (e) {
    if (selectedObjectIndex === null) return;

    const pos = objectPositions[selectedObjectIndex];
    switch (e.key) {
        case 'ArrowUp': pos.y -= 5; break;
        case 'ArrowDown': pos.y += 5; break;
        case 'ArrowLeft': pos.x -= 5; break;
        case 'ArrowRight': pos.x += 5; break;
        case '+':
            pos.width += 5;
            pos.height += 5;
            break;
        case '-':
            if (pos.width > 10 && pos.height > 10) {
                pos.width -= 5;
                pos.height -= 5;
            }
            break;
        default: return;
    }
    drawImages();
});
