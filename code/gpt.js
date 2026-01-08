/*
 * @Author: Victor-kawai 1900017878@pku.edu.cn
 * @Date: 2024-04-18 17:56:42
 * @LastEditors: Victor-kawai 1900017878@pku.edu.cn
 * @LastEditTime: 2024-04-18 18:28:18
 * @FilePath: \毕设\code\gpt.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
const treeData = {
  name: '总机构',
  type: 'organization', // 顶层节点是机构
  children: [
    {
      name: '分支机构1',
      type: 'organization', // 子节点是机构
      children: [
        { name: '部门1', type: 'position', children: [] }, // 子节点是官职
        {
          name: '子机构1',
          type: 'organization', // 子节点是机构
          children: [
            { name: '部门2', type: 'position', children: [] } // 子节点是官职
          ]
        }
      ]
    },
    {
      name: '分支机构2',
      type: 'organization', // 子节点是机构
      children: [
        { name: '部门3', type: 'position', children: [] }
      ]
    }
  ]
};

const width = 800;
const height = 600;

const svg = d3.select('body')
  .append('svg')
  .attr('width', width)
  .attr('height', height)
  .append('g')
  .attr('transform', 'translate(50, 50)');

const treeLayout = d3.tree().size([height - 100, width - 100]);
const root = d3.hierarchy(treeData);
const tree = treeLayout(root);

// 定义节点样式函数
const getNodeStyle = (d) => {
  return d.data.type === 'organization' ? 'fill: lightblue; stroke: blue;' : 'fill: lightgreen; stroke: green;';
};

// 添加连线
svg.selectAll('.link')
  .data(tree.links())
  .enter()
  .append('path')
  .attr('class', 'link')
  .attr('d', d3.linkVertical()
    .x(d => d.y)
    .y(d => d.x));

// 添加节点
const nodes = svg.selectAll('.node')
  .data(tree.descendants())
  .enter()
  .append('g')
  .attr('class', 'node')
  .attr('transform', d => `translate(${d.y},${d.x})`);

// 添加节点圆圈和文本
nodes.append('circle')
  .attr('r', 5)
  .attr('style', getNodeStyle);

nodes.append('text')
  .attr('dy', 3)
  .attr('x', d => d.children ? -8 : 8)
  .attr('text-anchor', d => d.children ? 'end' : 'start')
  .text(d => d.data.name);
