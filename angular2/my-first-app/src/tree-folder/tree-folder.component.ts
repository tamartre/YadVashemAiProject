import {ChangeDetectionStrategy, Component} from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {FlatTreeControl} from '@angular/cdk/tree';
import {MatTreeFlatDataSource, MatTreeFlattener, MatTreeModule} from '@angular/material/tree';
import {MatIconModule} from '@angular/material/icon';
interface FoodNode {
    name: string;
    children?: FoodNode[];
    // image?: string; // Add an optional image property to the FoodNode interface
  }

const TREE_DATA: FoodNode[] = [
    {
        name: 'Pictures',
        children: [{name: 'Mens'},] 
      },
    {
      name: 'documents',
      children: [
        {
          name: 'Ed',
          children: [{name: 'Broccoli', }],
        },
        {
          name: 'Orange',
          children: [{name: 'Pumpkins'}, {name: 'Carrots'}],
        },
      ],
    },
  ];



  /** Flat node with expandable and level information */
interface ExampleFlatNode {
    expandable: boolean;
    name: string;
    level: number;
  }
  
  /**
   * @title Tree with flat nodes
   */
@Component({
  selector: 'app-tree-folder',
  templateUrl: './tree-folder.component.html',
  styleUrl: './tree-folder.component.css',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatTreeModule, MatButtonModule, MatIconModule],
})
export class TreeFolderComponent {

  private _transformer = (node: FoodNode, level: number) => {
    return {
      expandable: !!node.children && node.children.length > 0,
      name: node.name,
      level: level,
    };
  };

  treeControl = new FlatTreeControl<ExampleFlatNode>(
    node => node.level,
    node => node.expandable,
  );

  treeFlattener = new MatTreeFlattener(
    this._transformer,
    node => node.level,
    node => node.expandable,
    node => node.children,
  );

  dataSource = new MatTreeFlatDataSource(this.treeControl, this.treeFlattener);

  constructor() {
    this.dataSource.data = TREE_DATA;
  }

  hasChild = (_: number, node: ExampleFlatNode) => node.expandable;
}

